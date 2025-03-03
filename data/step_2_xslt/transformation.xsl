<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0">

    <xsl:output method="text"/>

    <xsl:template match="/">
        <xsl:apply-templates select="//tei:w"/>
    </xsl:template>

    <xsl:template match="tei:w">
        <xsl:if test="not(@join='left')">
            <xsl:text> </xsl:text>
        </xsl:if>
        <xsl:value-of select="@norm"/>
    </xsl:template>

</xsl:stylesheet>

