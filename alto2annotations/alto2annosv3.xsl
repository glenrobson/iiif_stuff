<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
            xmlns:alto="http://www.loc.gov/standards/alto/ns-v3#"> <!-- note this namespace may need to change for different versions of ALTO -->
    <xsl:output method="text"/>
    <!-- This needs to resolve to the annotation list: -->
    <xsl:param name="annoURI" select="'http://localhost:8888/examples/anno_list.json'"/>

    <!--
        The ALTO may have been generated from the TIFF, if so the jp2 or IIIF image might be a different size. If so
        use the following ratios to reduce the TIFF coordinators to the IIIF image coordinates:
    -->
    <xsl:param name="xRatio" select="'3'"/>
    <xsl:param name="yRatio" select="'3'"/>

    <!-- Links to the canvas for the annotation and the manifest for the within -->
    <xsl:param name="canvasURI" select="'http://dams.llgc.org.uk/iiif/3320640/canvas/3320641'" />
    <!--
        Include this if you want to have a within link in the annotation. For example:
        <xsl:param name="manifestURI" select="'http://dams.llgc.org.uk/iiif/3100186/manifest.json'"/>
    -->
    <xsl:param name="manifestURI" />

    <xsl:variable name="quote">'</xsl:variable>
    <xsl:variable name="doubleqoute">"</xsl:variable>

    <xsl:template match="/">
        {
            "@context":"http://iiif.io/api/presentation/3/context.json",
            "id":"<xsl:value-of select="$annoURI"/>",
            "type":"AnnotationPage",
            "items":[
                <!--
                    If you want word level annotations use the following:
                <xsl:for-each select="/alto:alto/alto:Layout/alto:Page/alto:PrintSpace//alto:TextBlock//alto:TextLine/*">
                -->
                    <xsl:for-each select="/alto:alto/alto:Layout/alto:Page/alto:PrintSpace//alto:TextBlock//alto:TextLine">
                    {
                        "id": "<xsl:value-of select="$annoURI"/>-<xsl:value-of select="position()"/>",
                        "type":"Annotation",
                        "motivation":"commenting",
                        "body":
                        {
                            "type":"TextualBody",
                            "format":"text/plain",
                            <xsl:variable name="text">
                                <xsl:choose>
                                    <xsl:when test="name(.) = 'String'">
                                        <xsl:value-of select="./@CONTENT"/>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <xsl:apply-templates/>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </xsl:variable>
                    "value":"<xsl:call-template name="replace-string">
                        <xsl:with-param name="text">
                            <xsl:call-template name="replace-string">
                                <xsl:with-param name="text" select="normalize-space($text)" />
                                <xsl:with-param name="replace" select="'\'"/>
                                <xsl:with-param name="with" select="'\\'"/>
                            </xsl:call-template>
                        </xsl:with-param>
                        <xsl:with-param name="replace" select="$doubleqoute"/>
                        <xsl:with-param name="with" select="concat('\', $doubleqoute)"/>
                    </xsl:call-template>"
                        },
                        "target":"<xsl:value-of select="$canvasURI"/>#xywh=<xsl:value-of select="@HPOS div $xRatio"/>,<xsl:value-of select="@VPOS div $yRatio"/>,<xsl:value-of select="@WIDTH div $xRatio"/>,<xsl:value-of select="@HEIGHT div $yRatio"/>"
                        <xsl:if test="$manifestURI and string-length(normalize-space($manifestURI)) > 0">
                            ,
                            "partOf":
        					{
        						"id": "<xsl:value-of select="$manifestURI"/>",
        						"type": "Manifest"
        					}
                        </xsl:if>
                    }<xsl:if test="position() != last()">,</xsl:if>
                </xsl:for-each>
            ]
        }
    </xsl:template>
    <xsl:template match="alto:String">
        <xsl:value-of select="./@CONTENT"/>
    </xsl:template>
    <xsl:template match="alto:SP">
        <xsl:text> </xsl:text>
    </xsl:template>
    <xsl:template name="replace-string">
        <xsl:param name="text"/>
        <xsl:param name="replace"/>
        <xsl:param name="with"/>
        <xsl:choose>
            <xsl:when test="contains($text,$replace)">
                <xsl:value-of select="substring-before($text,$replace)"/>
                <xsl:value-of select="$with"/>
                <xsl:call-template name="replace-string">
                    <xsl:with-param name="text"
                        select="substring-after($text,$replace)"/>
                    <xsl:with-param name="replace" select="$replace"/>
                    <xsl:with-param name="with" select="$with"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$text"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>
